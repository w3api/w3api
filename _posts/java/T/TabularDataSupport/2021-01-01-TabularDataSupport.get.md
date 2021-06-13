---
title: TabularDataSupport.get()
permalink: /Java/TabularDataSupport/get/
date: 2021-01-11
key: Java.T.TabularDataSupport
category: Java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularDataSupport.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object get(Object key)
public CompositeData get(Object[] key)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}
* **Object[] key**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TabularDataSupport](/Java/TabularDataSupport/)

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
