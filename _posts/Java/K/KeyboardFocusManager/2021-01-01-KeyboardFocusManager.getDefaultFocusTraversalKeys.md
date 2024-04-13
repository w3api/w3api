---
title: KeyboardFocusManager.getDefaultFocusTraversalKeys()
permalink: /Java/KeyboardFocusManager/getDefaultFocusTraversalKeys/
date: 2021-01-11
key: Java.K.KeyboardFocusManager
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyboardFocusManager.metodos valor="getDefaultFocusTraversalKeys" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Set<AWTKeyStroke> getDefaultFocusTraversalKeys(int id)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KeyboardFocusManager](/Java/KeyboardFocusManager/)

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
