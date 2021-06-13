---
title: DefaultKeyboardFocusManager.enqueueKeyEvents()
permalink: /Java/DefaultKeyboardFocusManager/enqueueKeyEvents/
date: 2021-01-11
key: Java.D.DefaultKeyboardFocusManager
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultKeyboardFocusManager.metodos valor="enqueueKeyEvents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void enqueueKeyEvents(long after, Component untilFocused)
~~~

## Parámetros
* **Component untilFocused**,  {% include w3api/param_description.html metodo=_dato parametro="Component untilFocused" %}
* **long after**,  {% include w3api/param_description.html metodo=_dato parametro="long after" %}

## Clase Padre
[DefaultKeyboardFocusManager](/Java/DefaultKeyboardFocusManager/)

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
