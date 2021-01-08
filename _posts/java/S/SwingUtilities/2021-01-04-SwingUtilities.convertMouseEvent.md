---
title: SwingUtilities.convertMouseEvent()
permalink: Java/SwingUtilities/convertMouseEvent
date: 2021-01-04
key: JavaJava.S.SwingUtilities
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingUtilities.metodos valor="convertMouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MouseEvent convertMouseEvent(Component source, MouseEvent sourceEvent, Component destination)
~~~

## Parámetros
* **MouseEvent sourceEvent**,  {% include w3api/param_description.html metodo=_data parametro="MouseEvent sourceEvent" %}
* **Component destination**,  {% include w3api/param_description.html metodo=_data parametro="Component destination" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}

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
