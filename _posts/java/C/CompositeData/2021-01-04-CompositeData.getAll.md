---
title: CompositeData.getAll()
permalink: Java/CompositeData/getAll
date: 2021-01-04
key: JavaJava.C.CompositeData
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeData.metodos valor="getAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object[] getAll(String[] keys)
~~~

## Parámetros
* **String[] keys**,  {% include w3api/param_description.html metodo=_data parametro="String[] keys" %}

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
