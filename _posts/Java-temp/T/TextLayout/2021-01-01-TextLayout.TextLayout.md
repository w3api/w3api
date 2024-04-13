---
title: TextLayout.TextLayout()
permalink: /Java/TextLayout/TextLayout/
date: 2021-01-11
key: Java.T.TextLayout
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextLayout.constructores valor="TextLayout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextLayout(String string, Font font, FontRenderContext frc)
public TextLayout(String string, Map<? extends AttributedCharacterIterator.Attribute,?> attributes, FontRenderContext frc)
public TextLayout(AttributedCharacterIterator text, FontRenderContext frc)
~~~

## Parámetros
* **?&gt; attributes**,  {% include w3api/param_description.html metodo=_dato parametro="?> attributes" %}
* **Map&lt;? extends AttributedCharacterIterator.Attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends AttributedCharacterIterator.Attribute" %}
* **FontRenderContext frc**,  {% include w3api/param_description.html metodo=_dato parametro="FontRenderContext frc" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator text" %}
* **String string**,  {% include w3api/param_description.html metodo=_dato parametro="String string" %}
* **Font font**,  {% include w3api/param_description.html metodo=_dato parametro="Font font" %}

## Clase Padre
[TextLayout](/Java/TextLayout/)

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
