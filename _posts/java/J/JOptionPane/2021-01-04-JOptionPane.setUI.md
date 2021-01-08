---
title: JOptionPane.setUI()
permalink: Java/JOptionPane/setUI
date: 2021-01-04
key: JavaJava.J.JOptionPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, description="The UI object that implements the optionpane\'s LookAndFeel") public void setUI(OptionPaneUI ui)
~~~

## Parámetros
* **OptionPaneUI ui**,  {% include w3api/param_description.html metodo=_data parametro="OptionPaneUI ui" %}

## Clase Padre
[JOptionPane](/Java/JOptionPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JOptionPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
