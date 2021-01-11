---
title: KeyFactory.getKeySpec()
permalink: Java/KeyFactory/getKeySpec
date: 2021-01-11
key: JavaJava.K.KeyFactory
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyFactory.metodos valor="getKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends KeySpec>T getKeySpec(Key key, Class<T> keySpec)
~~~

## Parámetros
* **Class&lt;T&gt; keySpec**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> keySpec" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Clase Padre
[KeyFactory](/Java/KeyFactory/)

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
