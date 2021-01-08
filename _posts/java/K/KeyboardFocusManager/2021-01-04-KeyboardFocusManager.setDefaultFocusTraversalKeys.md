---
title: KeyboardFocusManager.setDefaultFocusTraversalKeys()
permalink: Java/KeyboardFocusManager/setDefaultFocusTraversalKeys
date: 2021-01-04
key: JavaJava.K.KeyboardFocusManager
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyboardFocusManager.metodos valor="setDefaultFocusTraversalKeys" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDefaultFocusTraversalKeys(int id, Set<? extends AWTKeyStroke> keystrokes)
~~~

## Parámetros
* **Set&lt;? extends AWTKeyStroke&gt; keystrokes**,  {% include w3api/param_description.html metodo=_data parametro="Set<? extends AWTKeyStroke> keystrokes" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}

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
{%- for _ldc in site.data.Java.K.KeyboardFocusManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
