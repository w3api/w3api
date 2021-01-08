---
title: CompositeData.get()
permalink: Java/CompositeData/get
date: 2021-01-04
key: JavaJava.C.CompositeData
category: java
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
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CompositeData](/Java/CompositeData/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
