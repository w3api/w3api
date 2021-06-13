---
title: ReferenceType.getValues()
permalink: /Java/ReferenceType-com-sun-jdi/getValues/
date: 2021-01-11
key: Java.R.ReferenceType-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceType-com-sun-jdi.metodos valor="getValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Map<Field,Value> getValues(List<? extends Field> fields)
~~~

## Parámetros
* **List&lt;? extends Field&gt; fields**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Field> fields" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [VMMismatchException](/Java/VMMismatchException/)

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
