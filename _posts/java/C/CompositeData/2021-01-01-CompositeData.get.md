---
title: CompositeData.get()
permalink: /Java/CompositeData/get/
date: 2021-01-11
key: Java.C.CompositeData
category: Java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeData.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object get(String key)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[CompositeData](/Java/CompositeData/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
