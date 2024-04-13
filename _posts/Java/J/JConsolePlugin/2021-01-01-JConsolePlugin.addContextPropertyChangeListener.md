---
title: JConsolePlugin.addContextPropertyChangeListener()
permalink: /Java/JConsolePlugin/addContextPropertyChangeListener/
date: 2021-01-11
key: Java.J.JConsolePlugin
category: Java
tags: ['java se', 'com.sun.tools.jconsole', 'jdk.jconsole', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JConsolePlugin.metodos valor="addContextPropertyChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void addContextPropertyChangeListener(PropertyChangeListener listener)
~~~

## Parámetros
* **PropertyChangeListener listener**,  {% include w3api/param_description.html metodo=_dato parametro="PropertyChangeListener listener" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JConsolePlugin](/Java/JConsolePlugin/)

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
