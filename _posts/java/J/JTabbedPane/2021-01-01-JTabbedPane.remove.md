---
title: JTabbedPane.remove()
permalink: /Java/JTabbedPane/remove/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void remove(int index)
public void remove(Component component)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
