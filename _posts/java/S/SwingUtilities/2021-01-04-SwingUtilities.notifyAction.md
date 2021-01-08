---
title: SwingUtilities.notifyAction()
permalink: Java/SwingUtilities/notifyAction
date: 2021-01-04
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
* **KeyEvent event**,  {% include w3api/param_description.html metodo=_data parametro="KeyEvent event" %}
* **KeyStroke ks**,  {% include w3api/param_description.html metodo=_data parametro="KeyStroke ks" %}
* **Action action**,  {% include w3api/param_description.html metodo=_data parametro="Action action" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **Object sender**,  {% include w3api/param_description.html metodo=_data parametro="Object sender" %}

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SwingUtilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
