---
title: ReferenceType.allLineLocations()
permalink: Java/ReferenceType-com-sun-jdi/allLineLocations
date: 2021-01-11
key: JavaJava.R.ReferenceType-com-sun-jdi
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceType-com-sun-jdi.metodos valor="allLineLocations" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<Location> allLineLocations() throws AbsentInformationException
List<Location> allLineLocations(String stratum, String sourceName) throws AbsentInformationException
~~~

## Parámetros
* **String stratum**,  {% include w3api/param_description.html metodo=_dato parametro="String stratum" %}
* **String sourceName**,  {% include w3api/param_description.html metodo=_dato parametro="String sourceName" %}

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
