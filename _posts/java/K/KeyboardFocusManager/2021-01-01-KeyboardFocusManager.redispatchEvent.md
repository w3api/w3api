---
title: KeyboardFocusManager.redispatchEvent()
permalink: /Java/KeyboardFocusManager/redispatchEvent/
date: 2021-01-11
key: Java.K.KeyboardFocusManager
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyboardFocusManager.metodos valor="redispatchEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void redispatchEvent(Component target, AWTEvent e)
~~~

## Parámetros
* **AWTEvent e**,  {% include w3api/param_description.html metodo=_dato parametro="AWTEvent e" %}
* **Component target**,  {% include w3api/param_description.html metodo=_dato parametro="Component target" %}

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
