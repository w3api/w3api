---
title: JComboBox.setEditor()
permalink: Java/JComboBox/setEditor
date: 2021-01-04
key: JavaJava.J.JComboBox
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComboBox.metodos valor="setEditor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(expert=true, description="The editor that combo box uses to edit the current value") public void setEditor(ComboBoxEditor anEditor)
~~~

## Parámetros
* **ComboBoxEditor anEditor**,  {% include w3api/param_description.html metodo=_data parametro="ComboBoxEditor anEditor" %}

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
