---
title: SortControl.SortControl()
permalink: /Java/SortControl/SortControl/
date: 2021-01-11
key: Java.S.SortControl
category: Java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SortControl.constructores valor="SortControl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SortControl(String[] sortBy, boolean criticality) throws IOException
public SortControl(String sortBy, boolean criticality) throws IOException
public SortControl(SortKey[] sortBy, boolean criticality) throws IOException
~~~

## Parámetros
* **boolean criticality**,  {% include w3api/param_description.html metodo=_dato parametro="boolean criticality" %}
* **String sortBy**,  {% include w3api/param_description.html metodo=_dato parametro="String sortBy" %}
* **SortKey[] sortBy**,  {% include w3api/param_description.html metodo=_dato parametro="SortKey[] sortBy" %}
* **String[] sortBy**,  {% include w3api/param_description.html metodo=_dato parametro="String[] sortBy" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[SortControl](/Java/SortControl/)

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
