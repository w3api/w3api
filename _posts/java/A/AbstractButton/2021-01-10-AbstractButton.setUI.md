---
title: AbstractButton.setUI()
permalink: Java/AbstractButton/setUI
date: 2021-01-10
key: JavaJava.A.AbstractButton
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the LookAndFeel.") public void setUI(ButtonUI ui)
~~~

## Parámetros
* **ButtonUI ui**,  {% include w3api/param_description.html metodo=_dato parametro="ButtonUI ui" %}

## Clase Padre
[AbstractButton](/Java/AbstractButton/)

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
