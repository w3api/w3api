---
title: ResourceBundle.Control.getTimeToLive()
permalink: Java/ResourceBundle/Control/getTimeToLive
date: 2021-01-11
key: Java.R.ResourceBundle.Control
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundle.Control.metodos valor="getTimeToLive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long getTimeToLive(String baseName, Locale locale)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ResourceBundle.Control](/Java/ResourceBundle/Control/)

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
