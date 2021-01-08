---
title: JOptionPane.showInternalOptionDialog()
permalink: Java/JOptionPane/showInternalOptionDialog
date: 2021-01-04
key: JavaJava.J.JOptionPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="showInternalOptionDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int showInternalOptionDialog(Component parentComponent, Object message, String title, int optionType, int messageType, Icon icon, Object[] options, Object initialValue)
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **Object message**,  {% include w3api/param_description.html metodo=_data parametro="Object message" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_data parametro="int messageType" %}
* **Object[] options**,  {% include w3api/param_description.html metodo=_data parametro="Object[] options" %}
* **Object initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Object initialValue" %}
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_data parametro="Component parentComponent" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}
* **int optionType**,  {% include w3api/param_description.html metodo=_data parametro="int optionType" %}

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
