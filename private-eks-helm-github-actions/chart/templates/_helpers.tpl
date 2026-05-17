{{- define "my-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "my-app.fullname" -}}
{{- printf "%s" (include "my-app.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
