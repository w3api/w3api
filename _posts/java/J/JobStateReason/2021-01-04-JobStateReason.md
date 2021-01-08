---
title: JobStateReason
permalink: Java/JobStateReason
date: 2021-01-04
key: JavaJava.J.JobStateReason
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JobStateReason.description }}

## Sintaxis
~~~java
public class JobStateReason extends EnumSyntax implements Attribute
~~~

## Constructores
* [JobStateReason()](/Java/JobStateReason/JobStateReason/)

## Campos
* [ABORTED_BY_SYSTEM](/Java/JobStateReason/ABORTED_BY_SYSTEM)
* [COMPRESSION_ERROR](/Java/JobStateReason/COMPRESSION_ERROR)
* [DOCUMENT_ACCESS_ERROR](/Java/JobStateReason/DOCUMENT_ACCESS_ERROR)
* [DOCUMENT_FORMAT_ERROR](/Java/JobStateReason/DOCUMENT_FORMAT_ERROR)
* [JOB_CANCELED_AT_DEVICE](/Java/JobStateReason/JOB_CANCELED_AT_DEVICE)
* [JOB_CANCELED_BY_OPERATOR](/Java/JobStateReason/JOB_CANCELED_BY_OPERATOR)
* [JOB_CANCELED_BY_USER](/Java/JobStateReason/JOB_CANCELED_BY_USER)
* [JOB_COMPLETED_SUCCESSFULLY](/Java/JobStateReason/JOB_COMPLETED_SUCCESSFULLY)
* [JOB_COMPLETED_WITH_ERRORS](/Java/JobStateReason/JOB_COMPLETED_WITH_ERRORS)
* [JOB_COMPLETED_WITH_WARNINGS](/Java/JobStateReason/JOB_COMPLETED_WITH_WARNINGS)
* [JOB_DATA_INSUFFICIENT](/Java/JobStateReason/JOB_DATA_INSUFFICIENT)
* [JOB_HOLD_UNTIL_SPECIFIED](/Java/JobStateReason/JOB_HOLD_UNTIL_SPECIFIED)
* [JOB_INCOMING](/Java/JobStateReason/JOB_INCOMING)
* [JOB_INTERPRETING](/Java/JobStateReason/JOB_INTERPRETING)
* [JOB_OUTGOING](/Java/JobStateReason/JOB_OUTGOING)
* [JOB_PRINTING](/Java/JobStateReason/JOB_PRINTING)
* [JOB_QUEUED](/Java/JobStateReason/JOB_QUEUED)
* [JOB_QUEUED_FOR_MARKER](/Java/JobStateReason/JOB_QUEUED_FOR_MARKER)
* [JOB_RESTARTABLE](/Java/JobStateReason/JOB_RESTARTABLE)
* [JOB_TRANSFORMING](/Java/JobStateReason/JOB_TRANSFORMING)
* [PRINTER_STOPPED](/Java/JobStateReason/PRINTER_STOPPED)
* [PRINTER_STOPPED_PARTLY](/Java/JobStateReason/PRINTER_STOPPED_PARTLY)
* [PROCESSING_TO_STOP_POINT](/Java/JobStateReason/PROCESSING_TO_STOP_POINT)
* [QUEUED_IN_DEVICE](/Java/JobStateReason/QUEUED_IN_DEVICE)
* [RESOURCES_ARE_NOT_READY](/Java/JobStateReason/RESOURCES_ARE_NOT_READY)
* [SERVICE_OFF_LINE](/Java/JobStateReason/SERVICE_OFF_LINE)
* [SUBMISSION_INTERRUPTED](/Java/JobStateReason/SUBMISSION_INTERRUPTED)
* [UNSUPPORTED_COMPRESSION](/Java/JobStateReason/UNSUPPORTED_COMPRESSION)
* [UNSUPPORTED_DOCUMENT_FORMAT](/Java/JobStateReason/UNSUPPORTED_DOCUMENT_FORMAT)

## Métodos
* [getCategory()](/Java/JobStateReason/getCategory)
* [getEnumValueTable()](/Java/JobStateReason/getEnumValueTable)
* [getName()](/Java/JobStateReason/getName)
* [getStringTable()](/Java/JobStateReason/getStringTable)

## Ejemplo
~~~java
{{ site.data.Java.J.JobStateReason.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JobStateReason.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
