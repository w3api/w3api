---
title: ReferenceType.locationsOfLine()
permalink: /Java/ReferenceType-com-sun-jdi/locationsOfLine/
date: 2021-01-11
key: Java.R.ReferenceType-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceType-com-sun-jdi.metodos valor="locationsOfLine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<Location> locationsOfLine(int lineNumber) throws AbsentInformationException
List<Location> locationsOfLine(String stratum, String sourceName, int lineNumber) throws AbsentInformationException
~~~

## Parámetros
* **String stratum**,  {% include w3api/param_description.html metodo=_dato parametro="String stratum" %}
* **String sourceName**,  {% include w3api/param_description.html metodo=_dato parametro="String sourceName" %}
* **int lineNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int lineNumber" %}

## Excepciones
[ClassNotPreparedException](/Java/ClassNotPreparedException/), [AbsentInformationException](/Java/AbsentInformationException/)

## Clase Padre
[ReferenceType](/Java/ReferenceType-com-sun-jdi/)

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
