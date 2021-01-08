---
title: JobAttributes.JobAttributes()
permalink: Java/JobAttributes/JobAttributes
date: 2021-01-04
key: JavaJava.J.JobAttributes
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JobAttributes.constructores valor="JobAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JobAttributes()
public JobAttributes(int copies, JobAttributes.DefaultSelectionType defaultSelection, JobAttributes.DestinationType destination, JobAttributes.DialogType dialog, String fileName, int maxPage, int minPage, JobAttributes.MultipleDocumentHandlingType multipleDocumentHandling, int[][] pageRanges, String printer, JobAttributes.SidesType sides)
public JobAttributes(JobAttributes obj)
~~~

## Parámetros
* **int minPage**,  {% include w3api/param_description.html metodo=_data parametro="int minPage" %}
* **JobAttributes.DestinationType destination**,  {% include w3api/param_description.html metodo=_data parametro="JobAttributes.DestinationType destination" %}
* **JobAttributes.SidesType sides**,  {% include w3api/param_description.html metodo=_data parametro="JobAttributes.SidesType sides" %}
* **JobAttributes.DialogType dialog**,  {% include w3api/param_description.html metodo=_data parametro="JobAttributes.DialogType dialog" %}
* **int maxPage**,  {% include w3api/param_description.html metodo=_data parametro="int maxPage" %}
* **int copies**,  {% include w3api/param_description.html metodo=_data parametro="int copies" %}
* **JobAttributes.DefaultSelectionType defaultSelection**,  {% include w3api/param_description.html metodo=_data parametro="JobAttributes.DefaultSelectionType defaultSelection" %}
* **String printer**,  {% include w3api/param_description.html metodo=_data parametro="String printer" %}
* **int[][] pageRanges**,  {% include w3api/param_description.html metodo=_data parametro="int[][] pageRanges" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **JobAttributes obj**,  {% include w3api/param_description.html metodo=_data parametro="JobAttributes obj" %}
* **JobAttributes.MultipleDocumentHandlingType multipleDocumentHandling**,  {% include w3api/param_description.html metodo=_data parametro="JobAttributes.MultipleDocumentHandlingType multipleDocumentHandling" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JobAttributes](/Java/JobAttributes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JobAttributes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
