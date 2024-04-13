---
title: Container.setFocusTraversalKeys()
permalink: /Java/Container/setFocusTraversalKeys/
date: 2021-01-11
key: Java.C.Container
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="setFocusTraversalKeys" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFocusTraversalKeys(int id, Set<? extends AWTKeyStroke> keystrokes)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Set&lt;? extends AWTKeyStroke&gt; keystrokes**,  {% include w3api/param_description.html metodo=_dato parametro="Set<? extends AWTKeyStroke> keystrokes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Container](/Java/Container/)

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
