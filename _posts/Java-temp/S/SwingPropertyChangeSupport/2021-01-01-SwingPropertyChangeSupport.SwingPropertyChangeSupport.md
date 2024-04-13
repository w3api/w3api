---
title: SwingPropertyChangeSupport.SwingPropertyChangeSupport()
permalink: /Java/SwingPropertyChangeSupport/SwingPropertyChangeSupport/
date: 2021-01-11
key: Java.S.SwingPropertyChangeSupport
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingPropertyChangeSupport.constructores valor="SwingPropertyChangeSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SwingPropertyChangeSupport(Object sourceBean)
public SwingPropertyChangeSupport(Object sourceBean, boolean notifyOnEDT)
~~~

## Parámetros
* **boolean notifyOnEDT**,  {% include w3api/param_description.html metodo=_dato parametro="boolean notifyOnEDT" %}
* **Object sourceBean**,  {% include w3api/param_description.html metodo=_dato parametro="Object sourceBean" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SwingPropertyChangeSupport](/Java/SwingPropertyChangeSupport/)

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
