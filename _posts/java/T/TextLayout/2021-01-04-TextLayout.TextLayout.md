---
title: TextLayout.TextLayout()
permalink: Java/TextLayout/TextLayout
date: 2021-01-04
key: JavaJava.T.TextLayout
category: java
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
* **?&gt; attributes**,  {% include w3api/param_description.html metodo=_data parametro="?> attributes" %}
* **FontRenderContext frc**,  {% include w3api/param_description.html metodo=_data parametro="FontRenderContext frc" %}
* **String string**,  {% include w3api/param_description.html metodo=_data parametro="String string" %}
* **Map&lt;? extends AttributedCharacterIterator.Attribute**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends AttributedCharacterIterator.Attribute" %}
* **Font font**,  {% include w3api/param_description.html metodo=_data parametro="Font font" %}
* **AttributedCharacterIterator text**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator text" %}

## Clase Padre
[TextLayout](/Java/TextLayout/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TextLayout.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
