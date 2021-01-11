---
title: AbstractButton.setMnemonic()
permalink: Java/AbstractButton/setMnemonic
date: 2021-01-11
key: JavaJava.A.AbstractButton
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setMnemonic" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, description="the keyboard character mnemonic") public void setMnemonic(char mnemonic)
@BeanProperty(visualUpdate=true, description="the keyboard character mnemonic") public void setMnemonic(int mnemonic)
~~~

## Parámetros
* **char mnemonic**,  {% include w3api/param_description.html metodo=_dato parametro="char mnemonic" %}
* **int mnemonic**,  {% include w3api/param_description.html metodo=_dato parametro="int mnemonic" %}

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
