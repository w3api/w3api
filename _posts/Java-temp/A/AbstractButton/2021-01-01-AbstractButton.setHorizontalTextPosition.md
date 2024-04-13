---
title: AbstractButton.setHorizontalTextPosition()
permalink: /Java/AbstractButton/setHorizontalTextPosition/
date: 2021-01-11
key: Java.A.AbstractButton
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setHorizontalTextPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, enumerationValues={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"}, description="The horizontal position of the text relative to the icon.") public void setHorizontalTextPosition(int textPosition)
~~~

## Parámetros
* **int textPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int textPosition" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
