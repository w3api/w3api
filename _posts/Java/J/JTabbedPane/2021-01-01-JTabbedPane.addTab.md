---
title: JTabbedPane.addTab()
permalink: /Java/JTabbedPane/addTab/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="addTab" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addTab(String title, Component component)
public void addTab(String title, Icon icon, Component component)
public void addTab(String title, Icon icon, Component component, String tip)
~~~

## Parámetros
* **String tip**,  {% include w3api/param_description.html metodo=_dato parametro="String tip" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
