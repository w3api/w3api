---
title: JobAttributes.JobAttributes()
permalink: /Java/JobAttributes/JobAttributes/
date: 2021-01-11
key: Java.J.JobAttributes
category: Java
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
* **JobAttributes.DialogType dialog**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.DialogType dialog" %}
* **JobAttributes.MultipleDocumentHandlingType multipleDocumentHandling**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.MultipleDocumentHandlingType multipleDocumentHandling" %}
* **String printer**,  {% include w3api/param_description.html metodo=_dato parametro="String printer" %}
* **int copies**,  {% include w3api/param_description.html metodo=_dato parametro="int copies" %}
* **int minPage**,  {% include w3api/param_description.html metodo=_dato parametro="int minPage" %}
* **JobAttributes.DefaultSelectionType defaultSelection**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.DefaultSelectionType defaultSelection" %}
* **JobAttributes obj**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes obj" %}
* **JobAttributes.DestinationType destination**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.DestinationType destination" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **JobAttributes.SidesType sides**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.SidesType sides" %}
* **int[][] pageRanges**,  {% include w3api/param_description.html metodo=_dato parametro="int[][] pageRanges" %}
* **int maxPage**,  {% include w3api/param_description.html metodo=_dato parametro="int maxPage" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
