---
title: ObjectReference.referringObjects()
permalink: Java/ObjectReference/referringObjects
date: 2021-01-04
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
* **long maxReferrers**,  {% include w3api/param_description.html metodo=_data parametro="long maxReferrers" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ObjectReference](/Java/ObjectReference/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
