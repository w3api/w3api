---
title: DefaultCellEditor.DefaultCellEditor()
permalink: Java/DefaultCellEditor/DefaultCellEditor
date: 2021-01-11
key: JavaJava.D.DefaultCellEditor
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultCellEditor.constructores valor="DefaultCellEditor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DefaultCellEditor(JCheckBox checkBox)
public DefaultCellEditor(JComboBox<?> comboBox)
@ConstructorProperties("component") public DefaultCellEditor(JTextField textField)
~~~

## Parámetros
* **JTextField textField**,  {% include w3api/param_description.html metodo=_dato parametro="JTextField textField" %}
* **JComboBox&lt;?&gt; comboBox**,  {% include w3api/param_description.html metodo=_dato parametro="JComboBox<?> comboBox" %}
* **JCheckBox checkBox**,  {% include w3api/param_description.html metodo=_dato parametro="JCheckBox checkBox" %}

## Clase Padre
[DefaultCellEditor](/Java/DefaultCellEditor/)

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
