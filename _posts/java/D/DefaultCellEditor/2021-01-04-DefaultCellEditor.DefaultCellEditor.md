---
title: DefaultCellEditor.DefaultCellEditor()
permalink: Java/DefaultCellEditor/DefaultCellEditor
date: 2021-01-04
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
* **JCheckBox checkBox**,  {% include w3api/param_description.html metodo=_data parametro="JCheckBox checkBox" %}
* **JTextField textField**,  {% include w3api/param_description.html metodo=_data parametro="JTextField textField" %}
* **JComboBox&lt;?&gt; comboBox**,  {% include w3api/param_description.html metodo=_data parametro="JComboBox<?> comboBox" %}

## Clase Padre
[DefaultCellEditor](/Java/DefaultCellEditor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultCellEditor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
