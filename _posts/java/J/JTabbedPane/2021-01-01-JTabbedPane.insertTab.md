---
title: JTabbedPane.insertTab()
permalink: Java/JTabbedPane/insertTab
date: 2021-01-11
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="insertTab" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insertTab(String title, Icon icon, Component component, String tip, int index)
~~~

## Parámetros
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String tip**,  {% include w3api/param_description.html metodo=_dato parametro="String tip" %}

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
