---
title: ResourceBundle.getObject()
permalink: Java/ResourceBundle/getObject
date: 2021-01-11
key: Java.R.ResourceBundle
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundle.metodos valor="getObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Object getObject(String key)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}

## Excepciones
[MissingResourceException](/Java/MissingResourceException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ResourceBundle](/Java/ResourceBundle/)

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
