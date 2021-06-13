---
title: ObjectReference.referringObjects()
permalink: /Java/ObjectReference/referringObjects/
date: 2021-01-11
key: JavaJava.O.ObjectReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectReference.metodos valor="referringObjects" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<ObjectReference> referringObjects(long maxReferrers)
~~~

## Parámetros
* **long maxReferrers**,  {% include w3api/param_description.html metodo=_dato parametro="long maxReferrers" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ObjectReference](/Java/ObjectReference/)

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
