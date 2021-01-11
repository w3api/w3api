---
title: JOptionPane.showInternalOptionDialog()
permalink: Java/JOptionPane/showInternalOptionDialog
date: 2021-01-11
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
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parentComponent" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_dato parametro="int messageType" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Object[] options**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] options" %}
* **Object initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object initialValue" %}
* **Object message**,  {% include w3api/param_description.html metodo=_dato parametro="Object message" %}
* **int optionType**,  {% include w3api/param_description.html metodo=_dato parametro="int optionType" %}

## Clase Padre
[JOptionPane](/Java/JOptionPane/)

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
