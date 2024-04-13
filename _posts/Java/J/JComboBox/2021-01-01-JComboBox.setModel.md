---
title: JComboBox.setModel()
permalink: /Java/JComboBox/setModel/
date: 2021-01-11
key: Java.J.JComboBox
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComboBox.metodos valor="setModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="Model that the combo box uses to get data to display.") public void setModel(ComboBoxModel<E> aModel)
~~~

## Parámetros
* **ComboBoxModel&lt;E&gt; aModel**,  {% include w3api/param_description.html metodo=_dato parametro="ComboBoxModel<E> aModel" %}

## Clase Padre
[JComboBox](/Java/JComboBox/)

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
