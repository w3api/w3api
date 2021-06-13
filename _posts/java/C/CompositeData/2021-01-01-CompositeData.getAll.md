---
title: CompositeData.getAll()
permalink: /Java/CompositeData/getAll/
date: 2021-01-11
key: Java.C.CompositeData
category: Java
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
* **String[] keys**,  {% include w3api/param_description.html metodo=_dato parametro="String[] keys" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[CompositeData](/Java/CompositeData/)

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
