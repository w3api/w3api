---
title: JComboBox.setRenderer()
permalink: Java/JComboBox/setRenderer
date: 2021-01-04
key: JavaJava.J.JComboBox
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComboBox.metodos valor="setRenderer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(expert=true, description="The renderer that paints the item selected in the list.") public void setRenderer(ListCellRenderer<? super E> aRenderer)
~~~

## Parámetros
* **ListCellRenderer&lt;? super E&gt; aRenderer**,  {% include w3api/param_description.html metodo=_data parametro="ListCellRenderer<? super E> aRenderer" %}

## Clase Padre
[JComboBox](/Java/JComboBox/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JComboBox.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
