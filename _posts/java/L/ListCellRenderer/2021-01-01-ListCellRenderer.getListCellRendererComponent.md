---
title: ListCellRenderer.getListCellRendererComponent()
permalink: /Java/ListCellRenderer/getListCellRendererComponent/
date: 2021-01-11
key: Java.L.ListCellRenderer
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.ListCellRenderer.metodos valor="getListCellRendererComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Component getListCellRendererComponent(JList<? extends E> list, E value, int index, boolean isSelected, boolean cellHasFocus)
~~~

## Parámetros
* **JList&lt;? extends E&gt; list**,  {% include w3api/param_description.html metodo=_dato parametro="JList<? extends E> list" %}
* **E value**,  {% include w3api/param_description.html metodo=_dato parametro="E value" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSelected" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **boolean cellHasFocus**,  {% include w3api/param_description.html metodo=_dato parametro="boolean cellHasFocus" %}

## Clase Padre
[ListCellRenderer](/Java/ListCellRenderer/)

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
