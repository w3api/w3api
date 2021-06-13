---
title: JTextField.setHorizontalAlignment()
permalink: /Java/JTextField/setHorizontalAlignment/
date: 2021-01-11
key: Java.J.JTextField
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextField.metodos valor="setHorizontalAlignment" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, enumerationValues={"JTextField.LEFT","JTextField.CENTER","JTextField.RIGHT","JTextField.LEADING","JTextField.TRAILING"}, description="Set the field alignment to LEFT, CENTER, RIGHT, LEADING (the default) or TRAILING") public void setHorizontalAlignment(int alignment)
~~~

## Parámetros
* **int alignment**,  {% include w3api/param_description.html metodo=_dato parametro="int alignment" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextField](/Java/JTextField/)

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
