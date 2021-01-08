---
title: MenuElement.processKeyEvent()
permalink: Java/MenuElement/processKeyEvent
date: 2021-01-04
key: JavaJava.M.MenuElement
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MenuElement.metodos valor="processKeyEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void processKeyEvent(KeyEvent event, MenuElement[] path, MenuSelectionManager manager)
~~~

## Parámetros
* **MenuSelectionManager manager**,  {% include w3api/param_description.html metodo=_data parametro="MenuSelectionManager manager" %}
* **KeyEvent event**,  {% include w3api/param_description.html metodo=_data parametro="KeyEvent event" %}
* **MenuElement[] path**,  {% include w3api/param_description.html metodo=_data parametro="MenuElement[] path" %}

## Clase Padre
[MenuElement](/Java/MenuElement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MenuElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
