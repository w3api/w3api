---
title: JTabbedPane.insertTab()
permalink: Java/JTabbedPane/insertTab
date: 2021-01-04
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
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **Component component**,  {% include w3api/param_description.html metodo=_data parametro="Component component" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}
* **String tip**,  {% include w3api/param_description.html metodo=_data parametro="String tip" %}

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
{%- for _ldc in site.data.Java.J.JTabbedPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
