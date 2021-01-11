---
title: SwingUtilities.notifyAction()
permalink: Java/SwingUtilities/notifyAction
date: 2021-01-11
key: JavaJava.S.SwingUtilities
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingUtilities.metodos valor="notifyAction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean notifyAction(Action action, KeyStroke ks, KeyEvent event, Object sender, int modifiers)
~~~

## Parámetros
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **KeyStroke ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStroke ks" %}
* **KeyEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="KeyEvent event" %}
* **Action action**,  {% include w3api/param_description.html metodo=_dato parametro="Action action" %}
* **Object sender**,  {% include w3api/param_description.html metodo=_dato parametro="Object sender" %}

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

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
