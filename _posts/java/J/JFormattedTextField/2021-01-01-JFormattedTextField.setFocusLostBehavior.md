---
title: JFormattedTextField.setFocusLostBehavior()
permalink: /Java/JFormattedTextField/setFocusLostBehavior/
date: 2021-01-11
key: Java.J.JFormattedTextField
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFormattedTextField.metodos valor="setFocusLostBehavior" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, enumerationValues={"JFormattedTextField.COMMIT","JFormattedTextField.COMMIT_OR_REVERT","JFormattedTextField.REVERT","JFormattedTextField.PERSIST"}, description="Behavior when component loses focus") public void setFocusLostBehavior(int behavior)
~~~

## Parámetros
* **int behavior**,  {% include w3api/param_description.html metodo=_dato parametro="int behavior" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JFormattedTextField](/Java/JFormattedTextField/)

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
