---
title: JComboBox.setUI()
permalink: Java/JComboBox/setUI
date: 2021-01-04
key: JavaJava.J.JComboBox
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComboBox.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the Component\'s LookAndFeel.") public void setUI(ComboBoxUI ui)
~~~

## Parámetros
* **ComboBoxUI ui**,  {% include w3api/param_description.html metodo=_data parametro="ComboBoxUI ui" %}

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
