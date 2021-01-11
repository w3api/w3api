---
title: JTabbedPane.setDisplayedMnemonicIndexAt()
permalink: Java/JTabbedPane/setDisplayedMnemonicIndexAt
date: 2021-01-11
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setDisplayedMnemonicIndexAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, description="the index into the String to draw the keyboard character mnemonic at") public void setDisplayedMnemonicIndexAt(int tabIndex, int mnemonicIndex)
~~~

## Parámetros
* **int mnemonicIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int mnemonicIndex" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int tabIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
