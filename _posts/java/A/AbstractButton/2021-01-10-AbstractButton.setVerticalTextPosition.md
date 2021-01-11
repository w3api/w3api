---
title: AbstractButton.setVerticalTextPosition()
permalink: Java/AbstractButton/setVerticalTextPosition
date: 2021-01-10
key: JavaJava.A.AbstractButton
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setVerticalTextPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, enumerationValues={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"}, description="The vertical position of the text relative to the icon.") public void setVerticalTextPosition(int textPosition)
~~~

## Parámetros
* **int textPosition**,  {% include w3api/param_description.html metodo=_dato parametro="int textPosition" %}

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
