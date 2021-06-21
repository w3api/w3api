---
title: JTextField.setDocument()
permalink: /Java/JTextField/setDocument/
date: 2021-01-11
key: Java.J.JTextField
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextField.metodos valor="setDocument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(expert=true, description="the text document model") public void setDocument(Document doc)
~~~

## Parámetros
* **Document doc**,  {% include w3api/param_description.html metodo=_dato parametro="Document doc" %}

## Clase Padre
[JTextField](/Java/JTextField/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
