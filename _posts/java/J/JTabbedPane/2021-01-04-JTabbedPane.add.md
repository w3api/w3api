---
title: JTabbedPane.add()
permalink: Java/JTabbedPane/add
date: 2021-01-04
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component add(Component component)
public Component add(Component component, int index)
public void add(Component component, Object constraints)
public void add(Component component, Object constraints, int index)
public Component add(String title, Component component)
~~~

## Parámetros
* **Component component**,  {% include w3api/param_description.html metodo=_data parametro="Component component" %}
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **Object constraints**,  {% include w3api/param_description.html metodo=_data parametro="Object constraints" %}

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JTabbedPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
